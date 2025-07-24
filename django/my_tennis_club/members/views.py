from django.http import HttpResponse
from django.template import loader
from .models import Member, MemberForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.contrib import messages
from django.db import IntegrityError

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def members(request):
  ##########################################################################################
  #####################################  QuerySet ##########################################
  ##########################################################################################
  # all (In the example below we use the .all() method to get all the records and fields of the Member model)
  mydata = Member.objects.all()

  # The values() Method (The values() method allows you to return each object as a Python dictionary, with the names and values as key/value pairs)
  mydata = Member.objects.all().values()

  # Return Specific Columns (The values_list() method allows you to return only the columns that you specify)
  mydata = Member.objects.values_list('firstname')

  # Return Specific Rows (You can filter the search to only return specific rows/records, by using the filter() method)
  mydata = Member.objects.filter(firstname='Emil').values()

  # Filter with AND
  mydata = Member.objects.filter(lastname='Refsnes', id=2).values()

  # Filter with OR
  mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
  # Another common method is to import and use Q expressions:
  mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
  #######################################################################################################################################




  ##########################################################################################
  ####################################  Field Lookups ######################################
  ##########################################################################################
  # contains (Get all records that have the value "bias" in the firstname column)
  mydata = Member.objects.filter(firstname__contains='bias').values()

  # icontains (Do a case insensitive search for all records that have the value "ref" in the lastname column)
  mydata = Member.objects.filter(lastname__icontains='ref').values()

  # endswith (Get all records where firstname ends with the letter "s")
  mydata = Member.objects.filter(firstname__endswith='s').values()

  # iendswith (Get all records where firstname ends with the letter "s")
  mydata = Member.objects.filter(firstname__iendswith='s').values()

  # exact (Get all records where firstname is exactly "Emil")
  mydata = Member.objects.filter(firstname__exact='Emil').values()

  # iexact (Get all records where firstname is exactly "emil")
  mydata = Member.objects.filter(firstname__iexact='emil').values()

  # in (Get all records where firstname is one of the values in the list)
  mydata = Member.objects.filter(firstname__in=['Tobias', 'Linus', 'John']).values()

  # gt- greater than (Get all records where id is larger than 3)
  mydata = Member.objects.filter(id__gt=3).values()

  # gt - greater than, or equal to (Get all records where id is 3 or larger)
  mydata = Member.objects.filter(id__gte=3).values()

  # lt - less than (Get all records where id is less than 3)
  mydata = Member.objects.filter(id__lt=3).values()

  # lte - less than, or equal to (Get all records where id is 3 or less)
  mydata = Member.objects.filter(id__lte=3).values()

  # range (Get all records where id is between 2 and 4)
  mydata = Member.objects.filter(id__range=(2, 4)).values()

  # startswith (Get all records where firstname starts with the letter "S")
  mydata = Member.objects.filter(firstname__startswith='S').values()

  # istartswith (Get all records where firstname starts with the letter "s")
  mydata = Member.objects.filter(firstname__istartswith='s').values()


  ##########################################################################################
  #################################  QuerySet - Order By ###################################
  ##########################################################################################

  # Order By (To sort QuerySets, Django uses the order_by() method)
  mydata = Member.objects.all().order_by('firstname').values()

  # Descending Order (By default, the result is sorted ascending (the lowest value first), to change the direction to descending (the highest value first), use the minus sign (NOT), - in front of the field name)
  mydata = Member.objects.all().order_by('-firstname').values()

  # Multiple Order Bys (To order by more than one field, separate the fieldnames with a comma in the order_by() method)
  mydata = Member.objects.all().order_by('lastname', '-id').values()

  print(mydata)
  #######################################################################################################################################

  #Main
  #mymembers = Member.objects.all().values()
  mymembers = Member.objects.all().order_by('-id').values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, slug):
  try:
      mymember = Member.objects.get(slug=slug)
      template = loader.get_template('details.html')
      context = {
        'mymember': mymember
      }
      return HttpResponse(template.render(context, request))
  except Member.DoesNotExist:
      template = loader.get_template('404.html')
      return HttpResponse(template.render())
  
def add_member_form(request, member_id=None, pk=None):
    instance = None
    if pk:
        instance = get_object_or_404(Member, pk=pk)


    if member_id:
        member = get_object_or_404(Member, pk=member_id)
    else:
        member = None

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            obj = form.save(commit=False)
            # Generate slug if new or if name has changed
            if not obj.slug or (member and (obj.firstname != member.firstname or obj.lastname != member.lastname)):
                obj.slug = generate_unique_slug(obj.firstname, obj.lastname, instance=member)
            # Save the object
            obj.save()
            if pk:
                messages.success(request, 'Member updated successfully.')
            else:
                messages.success(request, 'Member added successfully.')
            return redirect('members')
    else:
        form = MemberForm(instance=member)

    return render(request, 'add_member.html', {
        'form': form,
        'member': member
    })

def delete_member(request, member_id):
    try:
        member = get_object_or_404(Member, pk=member_id)
        member.delete()
        messages.success(request, 'Member deleted successfully.')
    except IntegrityError:
        messages.error(request, 'Cannot delete this member due to related records.')
    except Exception as e:
        messages.error(request, f'Error deleting member : {str(e)}')

    return redirect('members')

def generate_unique_slug(firstname, lastname, instance=None):
  base_slug = slugify(f"{firstname}-{lastname}")
  slug = base_slug
  counter = 1

  # Filter existing slugs excluding the current instance
  while Member.objects.filter(slug=slug).exclude(pk=instance.pk if instance and instance.pk else None).exists():
      slug = f"{base_slug}-{counter}"
      counter += 1

  return slug